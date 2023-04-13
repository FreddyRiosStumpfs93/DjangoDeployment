$(function(){
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax:{
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "chapter"},
            {"data": "description"},
            {"data": "description"},
        ],
        columnDefs: [
            {
                targets: [3],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row){
                    var buttons = '<a href="/myapi/chapter/edit/'+row.id+'/" type="button" class="btn btn-warning btn-xs"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/myapi/chapter/delete/'+row.id+'/" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (setting, json){
        }
    });
});