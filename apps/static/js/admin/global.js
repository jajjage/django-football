$(function() {
    $('.field-price').each(function() {
        let value = parseFloat($(this).text());
        if (!isNaN(value)) {
            $(this).text('\u20AC' + value.toFixed(2));
        }
    });

    var concept_button = $('footer .actions .action-save');
    var publish_button = $('footer .actions ul button[value="action-publish"]');
    var publish_list_item = $(publish_button).parent();

    $(concept_button).after($(publish_button));
    $(concept_button).appendTo($(publish_list_item));

    // Get GET parameters and split the ordering on dot.
    var queryDict = {};
    location.search.substr(1).split("&").forEach(function(item) {queryDict[item.split("=")[0]] = item.split("=")[1]});

    // ordening GET parameter.
    if ('o' in queryDict) {
        var get_params = queryDict['o'].split(".");

        // Set superscript on ordering.
        var table_head_columns = $('table.listing thead tr th');
        for (var i = 0; i < get_params.length; i++) {

            number = get_params[i];
            if (number[0] === '-') {
                number = number.substring(1);
            }
            number = parseInt(number);

            column = table_head_columns[number];
            $(column).find('a').append('<sup>' + i + '</sup>')
        }
    }

    $('.new-line').parents('li').addClass('newline');

});