from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import BookUploadForm
from django.contrib.auth.decorators import login_required
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Book
from django.shortcuts import render
from .models import Book, Category, Scholar
from django.db.models import Q

def public_book_list(request):
    books = Book.objects.filter(status='approved')
    return render(request, 'library/public_books.html', {'books': books})



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Django's built-in login URL
    else:
        form = UserCreationForm()
    return render(request, 'library/signup.html', {'form': form})


@login_required
def contributor_dashboard(request):
    my_books = Book.objects.filter(uploaded_by=request.user)
    return render(request, 'library/contributor_dashboard.html', {'books': my_books})

@login_required
def upload_book(request):
    if request.method == 'POST':
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploaded_by = request.user
            book.status = 'pending'
            book.save()
            return redirect('upload_success')
    else:
        form = BookUploadForm()
    return render(request, 'library/upload_book.html', {'form': form})

def upload_success(request):
    return render(request, 'library/upload_success.html')


def public_books(request):
    query = request.GET.get('q', '')
    scholar_id = request.GET.get('scholar', '')
    category_id = request.GET.get('category', '')

    books = Book.objects.filter(status='approved')
    scholars = Scholar.objects.all()
    categories = Category.objects.all()

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(category__name__icontains=query) |
            Q(scholar__name__icontains=query)
        )

    if scholar_id:
        books = books.filter(scholar_id=scholar_id)

    if category_id:
        books = books.filter(category_id=category_id)

    return render(request, 'library/public_books.html', {
        'books': books,
        'query': query,
        'scholars': scholars,
        'categories': categories,
        'selected_scholar': scholar_id,
        'selected_category': category_id,
    })


def book_detail(request, book_id):
    book = Book.objects.filter(id=book_id, status='approved').first()
    if not book:
        return render(request, '404.html', status=404)

    return render(request, 'library/book_detail.html', {'book': book})


from django.contrib.admin.views.decorators import staff_member_required
from .forms import BookReviewForm

@staff_member_required
def review_books(request):
    pending_books = Book.objects.filter(status='pending')
    return render(request, 'library/review_books.html', {'books': pending_books})


@staff_member_required
def review_book_action(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = BookReviewForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('review_books')
    return redirect('review_books')


from django.shortcuts import get_object_or_404

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id, status='approved')
    return render(request, 'library/book_detail.html', {'book': book})

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'library/login.html'

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout_view(request):
    logout(request)
    return redirect('login')