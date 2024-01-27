$(document).ready(function () {
    const filter_object = {};

    $(".filter-checkbox").on("click", function () {
        console.log("A checkbox has been clicked");
        const category = []
        let filter_key = $(this).data("filter");

        // Iterate through checked checkboxes with the data-filter attribute set to 'category'
        $("input[data-filter='Category']:checked").each(function () {
            let filter_value = $(this).val();

            // Add each checked value to the category
            category.push(filter_value);
        });
        
        filter_object[filter_key] = category;

        console.log("filter object is", filter_object);
        filteringAjax(filter_object);
    });

    // Getting value form number input
    $(".price-input input").on("input", function() {
        let filter_key = $(this).data("filter");
        filter_object[filter_key] = $(this).val();

        debounce(filteringAjax, 500)(filter_object);
    })

    //Getting value from range input
    $(".range-input input").on("change", function() {
        let filter_key = $(this).data("filter");
        filter_object[filter_key] = $(this).val();

        debounce(filteringAjax, 500)(filter_object);
    })
});

function debounce(func, delay) {
    return function() {
        const context = this;
        const args = arguments;

        clearTimeout(window.timeoutId);
        window.timeoutId = setTimeout(function() {
            func.apply(context, args);
        }, delay);
    };
}


function filteringAjax(data) {
    $.ajax({
        url: '/filter-residences/',
        data: data,
        dataType: 'json',
        beforeSend: function () {
            console.log("Trying to filter residence...");
        },
        success: function (response) {
            console.log(response);
            console.log("Data filtered successfully.");
            $("#filtered-residences").html(response.data);
        },
        error: function (error) {
            console.log("Error during filtering:", error);
        }
    });
}
 