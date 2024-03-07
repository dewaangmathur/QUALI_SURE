

document.addEventListener("DOMContentLoaded", function () {
    const testForm = document.getElementById("testForm");
    const csvDataFile = document.getElementById("UploadFile");
    const productPage = document.querySelector('.product-page');
    const searchTermInput = document.querySelector('.searchTerm');
    const searchButton = document.querySelector('.searchButton');
    const weightCatButton = document.querySelector('.weight-cat-btn');
    const brands = ['Adidas', 'Nike', 'Puma', 'Armani', 'Van Heusen'];
    const highlySustainableFabrics = ['cotton', 'jute'];
    const midSustainableFabrics = ['polyester', 'nylon'];
    const lowSustainableFabrics = ['silk'];
    
    let allProducts; // for storing csvData
    
    testForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const input = csvDataFile.files[0];
        const reader = new FileReader();
        
        reader.onload = function (e) {
            const text = e.target.result;
            allProducts = d3.csvParse(text);
            //console.log(allProducts);
            appendProductCards(allProducts);
        };
        reader.readAsText(input);
    });
    let productStockAvailable = 0;
    
    function appendProductCards(products) {
        products.forEach(product => {
            const productCard = document.createElement('div');
    
            productCard.className = 'product-cards';
            productCard.setAttribute('data-prod-id', product['prod-id']);
            const productDescription = product['prod-desc'];
            let correctInformation = 0;
            if (productDescription.toLowerCase().indexOf('size') !== -1) {
                correctInformation = 1;
            }
                   
            console.log(productDescription.toLowerCase().indexOf(product['prod-title'].toLowerCase()));
            const productStockAvailable = parseFloat(product['prod-stock-available']);
            const productFactorThree = parseFloat(product['factor-three']);
            let productBrandWeight = 0;
            let productFabricWeight = 0;
            
            if(brands.includes(product['prod-title'])) {
                productBrandWeight = 1;
            }

            if(highlySustainableFabrics.includes(product['prod-fabric'])) {
                productFabricWeight = 1;
            } else if(midSustainableFabrics.includes(product['prod-fabric'])) {
                productFabricWeight = 0.5;
            } else {
                productFabricWeight = 0;
            }
            
            // let productConsumed = productStockAlloted-productStockAvailable;
            // const productPopularityWeight = productConsumed/productStockAlloted;
            const productWeight = parseInt(0.03*productStockAvailable+2*productFactorThree+5*productBrandWeight+2*productFabricWeight-8);
            
    
            const alertText = showAlertText(productWeight);
            if (productWeight < 1) {
                productCard.classList.add("red");
            } else if(productWeight < 2) {
                productCard.classList.add('yellow');
            } else {
                productCard.classList.add('green');
            }
            productCard.innerHTML = `<div class="product-img">
                <img src="${product['prod-img']}" alt="img" srcset="">
                </div>
                <div class="product-info">
                <h1 class="product-title">${product['prod-title']}</h1>
                <p class="product-desc">${product['prod-desc']}</p>
                <h2 class="price"><span>₹</span>${product['prod-price']}</h2>
                </div>
                <div class = "q-factor-box"><p>${productWeight}</p><h4>${alertText}</h4></div>`

            // const qFactorBox = document.querySelector('.q-factor-box');
            // if (productWeight < 0) {
            //     qFactorBox.classList.add('box-red');
            // } else if(productWeight < 2) {
            //     qFactorBox.classList.add('box-yellow');
            // } else {
            //     qFactorBox.classList.add('box-green');
            // }
            productPage.appendChild(productCard);
        });
    }
    
    
    searchButton.addEventListener('click', function () {
        const searchTerm = searchTermInput.value.trim().toLowerCase();
        const filteredProducts = filterProducts(searchTerm);
        productPage.innerHTML = '';
        appendProductCards(filteredProducts);
    });
    
    function filterProducts(searchTerm) {
        return allProducts.filter(product => {
            console.log(product);
            const productIdMatch = product['prod-id'].includes(searchTerm);
            const productTitleMatch = product['prod-title'].toLowerCase().includes(searchTerm);
            return productIdMatch || productTitleMatch;
      });
    }
    function showAlertText(number) {
        if(number < 1) {
            return "Not trusted";
        } else if(number < 2) {
            return "Can be risky to trust";
        } else {
            return "Can be trusted";
        }
    }

    // weightCatButton.addEventListener('click', function() {
    //     showProductsByColors('green');
    //     showProductsByColors('yellow');
    //     showProductsByColors('red');
    // })
    
    // function showProductsByColors(color) {
    //     const products = document.querySelectorAll('.product-cards');
    //     productPage.innerHTML = '';
    //     products.forEach(product => {
    //         if (product.classList.contains(color)) {
    //             const productIdMatch = product['prod-id'];
    //             console.log(productIdMatch);
    //             const filteredProducts = filterProducts(productIdMatch);
    //             appendProductCards(filteredProducts);
    //         }
    //     });
    // }
    
  });


  