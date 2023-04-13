var classification = {
    items: {
        description: '',
        material: '',
        classify: ''
    },
};

$(function(){
    // event submit
    $('form').on('submit', function (e) {
        e.preventDefault();
        classification.items.description = $('input[name="description"]').val();
        classification.items.material = $('select[name="material"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('classification', JSON.stringify(classification.items));
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            location.href = '{{ list_url }}';
        });
    });
});
