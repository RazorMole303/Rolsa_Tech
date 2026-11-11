from django.shortcuts import render, redirect
from .forms import RegistrationForm, StorePurchaseForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView

PRODUCTS = [
    {
        "id": "solar-panels",
        "name": "Solar Panels",
        "category": "Renewables",
        "price": "$4,200",
        "description": "High-efficiency rooftop and commercial solar systems built for long-term savings and reliability.",
        "features": ["450W monocrystalline panels", "Battery-ready inverters", "25-year performance warranty"],
    },
    {
        "id": "electric-cars",
        "name": "Electric Cars",
        "category": "Mobility",
        "price": "$32,500",
        "description": "Premium electric vehicles designed for city commuting, family travel, and lower operating costs.",
        "features": ["Fast charging support", "Range up to 420 miles", "Smart driving assistance"],
    },
    {
        "id": "wind-farms",
        "name": "Wind Farms",
        "category": "Utility Scale",
        "price": "$1.8M",
        "description": "Modular turbine packages for community energy projects and industrial-scale renewable power generation.",
        "features": ["3.5MW turbines", "Grid integration support", "Scalable deployment plans"],
    },
]

# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')


def about(request):
    return render(request, 'webpages/about.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account is ready. Please sign in.")
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})


class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        messages.success(request, "You have successfully logged out")
        return super().post(request, *args, **kwargs)


class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        messages.success(request, "You have successfully logged in")
        return super().post(request, *args, **kwargs)


def calculator(request):
    return render(request, "webpages/calculator.html")


def store(request):
    selected_product = request.GET.get("product")
    form = StorePurchaseForm(products=PRODUCTS)

    if request.method == "POST":
        form = StorePurchaseForm(request.POST, products=PRODUCTS)
        if form.is_valid():
            product_id = form.cleaned_data["product"]
            product = next((item for item in PRODUCTS if item["id"] == product_id), PRODUCTS[0])
            messages.success(
                request,
                f"Your order for {product['name']} has been received. Our team will contact you at {form.cleaned_data['email']} to confirm delivery and installation.",
            )
            return redirect("store")

    if selected_product:
        form.initial["product"] = selected_product

    return render(request, "webpages/store.html", {"products": PRODUCTS, "form": form, "selected_product": selected_product})


