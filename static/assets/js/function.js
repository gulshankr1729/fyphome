$(document).ready(function () {
    $(".filter-checkbox").on("click", function () {
        console.log("A checkbox has been clicked");

        let filter_object = {};

        // Iterate through checked checkboxes with the data-filter attribute set to 'category'
        $("input[data-filter='Category']:checked").each(function () {
            let filter_key = $(this).data("filter");
            let filter_value = $(this).val();

            console.log("filter value is:", filter_value);
            console.log("filter key is:", filter_key);

            // Add each checked value to the filter_object
            if (filter_key in filter_object) {
                filter_object[filter_key].push(filter_value);
            } else {
                filter_object[filter_key] = [filter_value];
            }
        });

        console.log("filter object is", filter_object);

        $.ajax({
            url: '/filter-residences/',
            data: filter_object,
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
    });
});
