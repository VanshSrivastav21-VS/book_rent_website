from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, Http404
from .models import Book
import stripe
import os


stripe.api_key = 'sk_test_51PXND22NNWfS0Rs5YezOnkHyk7JVsiWKckuUvqe7aGzFYo0pwIL8Ce2gQ7cFiOPmwbaHr4XVFvhckgEZCziKo55t00z930Tdrc'


# Create your views here.
def home(request):
    books = Book.objects.all()
    latest_books = Book.objects.order_by('-id')[:4]  # Fetch the latest 4 books based on their ID
    context = {'books': latest_books}
    return render(request, 'books/home.html', context)

def books(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'books/books.html', {'books': books})



def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/view_book.html',  {'book': book})

def rent_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        days = int(request.POST['days'])
        payment_option = request.POST['payment_option']

        if payment_option == 'buy':
            price = book.price
        else:
            price = book.rental_price * days / 3  # Adjust rental price based on the number of days

        # Save rental information or process payment here

        # Redirect to payment or success page
        return redirect('checkout', book_id=book.id)

    return render(request, 'books/rent_book.html', {'book': book})

def checkout(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Create a Stripe Checkout Session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': book.title,
                    },
                    'unit_amount': int(book.rental_price * 100),  # Amount in cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(f'/success/{book_id}/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
        return redirect(session.url, code=303)
    return render(request, 'books/checkout.html', {'book': book})

def success(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Any additional logic
    return render(request, 'books/success.html', {'book': book})

def download_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    # Check if the file exists
    if not book.pdf:
        raise Http404("File not found")
    
    file_path = book.pdf.path  # Make sure this is the correct field for the file
    
    # Ensure file exists before attempting to open
    if not os.path.exists(file_path):
        raise Http404("File not found")
    
    try:
        # Serve the file as an attachment
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=book.pdf.name)
        return response
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error downloading file: {e}")
        raise Http404("Something went wrong")
    




















def about(request):
    return render(request, 'books/about.html')