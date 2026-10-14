import pytest
from playwright.sync_api import Playwright,expect

# @pytest.mark.api
def test_getApi(playwright: Playwright):
    context = playwright.request.new_context()
    response = context.get("https://dummyjson.com/products?limit=5")
    # print(response.json())
    print(response.status)
    assert response.status == 200
    data = response.json()
    assert data["products"][0]["title"] == "iPhone 9"


# @pytest.mark.api
def test_getApi_auth(playwright: Playwright):
    context = playwright.request.new_context(http_credentials={"username": "admin", "password": "admin"})
    # response = context.get("https://dummyjson.com/products?limit=5", headers={"Authorization": "Bearer 123456"})
    # response = context.get("https://dummyjson.com/products?limit=5", headers={"x-api-key": "123456"})
    response = context.get("https://dummyjson.com/products?limit=5")


# @pytest.mark.api
def test_getApi(playwright: Playwright):
    context = playwright.request.new_context()
    requestBody = {
            "title": "playwright",
            "description": "The Essence Mascara Lash Princess is a popular mascara known for its volumizing and lengthening effects. Achieve dramatic lashes with this long-lasting and cruelty-free formula.",
            "category": "beauty",
            "discountPercentage": 10.48,
            "rating": 2.56,
            "stock": 99,
            "tags": [
                "beauty",
                "mascara"
            ],
            "brand": "Essence",
            "sku": "BEA-ESS-ESS-001",
            "weight": 4,
            "dimensions": {
                "width": 15.14,
                "height": 13.08,
                "depth": 22.99
            },
            "warrantyInformation": "1 week warranty",
            "shippingInformation": "Ships in 3-5 business days",
            "availabilityStatus": "In Stock",
            "reviews": [
                {
                    "rating": 3,
                    "comment": "Would not recommend!",
                    "date": "2025-04-30T09:41:02.053Z",
                    "reviewerName": "Eleanor Collins",
                    "reviewerEmail": "eleanor.collins@x.dummyjson.com"
                },
                {
                    "rating": 4,
                    "comment": "Very satisfied!",
                    "date": "2025-04-30T09:41:02.053Z",
                    "reviewerName": "Lucas Gordon",
                    "reviewerEmail": "lucas.gordon@x.dummyjson.com"
                },
                {
                    "rating": 5,
                    "comment": "Highly impressed!",
                    "date": "2025-04-30T09:41:02.053Z",
                    "reviewerName": "Eleanor Collins",
                    "reviewerEmail": "eleanor.collins@x.dummyjson.com"
                }
            ],
            "returnPolicy": "No return policy",
            "minimumOrderQuantity": 48,
            "meta": {
                "createdAt": "2025-10-09T14:47:01.588Z",
                "updatedAt": "2026-05-23T11:27:41.868Z",
                "barcode": "5784719087687",
                "qrCode": "https://cdn.dummyjson.com/public/qr-code.png"
            },
            "images": [
                "https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/1.webp"
            ],
            "thumbnail": "https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/thumbnail.webp"
        }
    response = context.post("https://dummyjson.com/products/add",headers={"Authorization": "Bearer 123456"}, data=requestBody)
    # print(response.json())
    print(response.status)
    assert response.status == 201

    

