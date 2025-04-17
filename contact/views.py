from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def contact_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ Save the form data to the database
            messages.success(request, "Thanks for contacting us! We’ll get back to you soon.")
            return redirect('contact')

    return render(request, 'contact/contact.html', {'form': form})