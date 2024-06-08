async function fetchData() {
    const api_get_most_liked_products = 'http://127.0.0.1:1010/api/get-most-liked-products'

    try {
        const response = await fetch(api_get_most_liked_products)

        if (!response.ok) {
            throw new Error(`HTTP ERROR: Status: ${response.status}`)
        }

        const data = await response.json()
        console.log(data)
        displayProducts(data)
    } catch (error) {
        console.log(error)
    }
}
function displayProducts(products) {
    const container = document.getElementById('product-container');
    container.innerHTML = '';

    for (let product in products) {
        const productBox = document.createElement('div')
        productBox.classList.add('product-box')

        const productImg = document.createElement('img')
        productImg.src = products[product][0]
        productImg.alt = product

        const nameAndwishlistIcon = document.createElement('div')
        nameAndwishlistIcon.classList.add('name-wishlistIcon')

        const productName = document.createElement('h3')
        productName.textContent = product

        const priceContainer = document.createElement('div')
        priceContainer.classList.add('price-container')

        const productPrice = document.createElement('p')
        productPrice.textContent = products[product][1]
        productPrice.classList.add('price')

        const add_to_cart = document.createElement('p')
        add_to_cart.textContent = 'Add to cart'
        add_to_cart.classList.add('add-to-cart')


        const wishlistIcon = document.createElement('i')
        wishlistIcon.classList.add('far')
        wishlistIcon.classList.add("fa-heart")
        
        nameAndwishlistIcon.appendChild(productName)
        nameAndwishlistIcon.appendChild(wishlistIcon)

        priceContainer.appendChild(productPrice)
        priceContainer.appendChild(add_to_cart)

        productBox.appendChild(productImg)
        productBox.appendChild(nameAndwishlistIcon)

        productBox.appendChild(priceContainer)

        container.append(productBox)
    }
}
window.onload = fetchData();

