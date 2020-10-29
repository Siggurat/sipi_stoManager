$(document).ready(function() {

    $(window).scroll(function() {
        var window_top = $(window).scrollTop();

        var servicesTop = $('#services').offset().top - 200,
            applicationTop = $('#application').offset().top - 200,
            trackAppTop = $('#trackApplication').offset().top - 370;

        if (window_top >= trackAppTop) {
            $('#menu li.active').removeClass('active');
            $('#menu a[href="#trackApplication"]').parent().addClass('active')
        }
        else if (window_top >= applicationTop) {
            $('#menu li.active').removeClass('active');
            $('#menu a[href="#application"]').parent().addClass('active')
        }
        else if (window_top >= servicesTop) {
            $('#menu li.active').removeClass('active');
            $('#menu a[href="#services"]').parent().addClass('active')
        }
        else {
            $('#menu li.active').removeClass('active');
            $('#menu a[href="#aboutUs"]').parent().addClass('active')
        }
    });

    $('#menu, .banner').on('click', 'a', function(e) {
        e.preventDefault();
        var id = $(this).attr('href'),
            top = $(id).offset().top - 71;

        $('body,html').animate({scrollTop: top}, 800);
    });

    $('select').niceSelect();

    $('#tel').mask('+7 (000) 000-00-00', {
        'translation': {
            0: {
                pattern: /[0-9*]/
            }
        }
    });

    $('#trackInput').mask('####-####-####-####', {
        'translation': {
            '#': {
                pattern: /[A-Za-z0-9]/
            }
        }
    });

    $('#car_brand').change(function() {
        let brand = $(this).val();
        let json_url = '/brand/' + brand;

        $.getJSON(json_url, function(data) {
            let optionHTML = '<option selected value="__None">Выберите модель</option>';

            for (let model of data.models) {
                optionHTML += '<option value="' + model.id + '">' + model.name + '</option>';
            }

            let car_model_select = $('#car_model');

            if (optionHTML !== '<option selected value="__None">Выберите модель</option>') {
                car_model_select.prop('disabled', false);
                car_model_select.html(optionHTML);
            } else {
                car_model_select.html(optionHTML);
                car_model_select.prop('disabled', true);
            }
            car_model_select.niceSelect('update');
        })
    });

    $('#form_app').submit(function(event) {

        const form_controls = {
            car_brand: {
                input: $('#car_brand'),
                error: $('#car_brand_error')
            },
            car_model: {
                input: $('#car_model'),
                error: $('#car_model_error')
            },
            name: {
                input: $('#name'),
                error: $('#name_error')
            },
            last_name: {
                input: $('#last_name'),
                error: $('#last_name_error')
            },
            email: {
                input: $('#email'),
                error: $('#email_error')
            },
            tel: {
              input: $('#tel'),
              error: $('#tel_error')
            }
        };

        form_controls.car_model.input.prop('disabled', false);

        $.ajax({
            data: {
                car_brand: form_controls.car_brand.input.val(),
                car_model: form_controls.car_model.input.val(),
                name: form_controls.name.input.val(),
                last_name: form_controls.last_name.input.val(),
                email: form_controls.email.input.val(),
                tel: form_controls.tel.input.val()
            },
            type: 'POST',
            url: '/register-app'
        })
            .done(function(data) {
                $('#form_app .alert-danger').addClass('d-none');
                if (data.errors) {
                    $.each(data.errors, function(error) {
                        form_controls[error].error.text(data.errors[error][0]).removeClass('d-none');
                        $('#app_form_success').addClass('d-none');
                    })
                } else {
                    $('#app_form_success').text(data.success).removeClass('d-none');
                }
            });

        event.preventDefault();
    });

    $('#getAppInfoBtn').click(function() {
        let track_number = $('#trackInput').val();
        let json_url = '/get-app-info/';

        if (track_number) {
            json_url += track_number;
        } else {
            json_url += 'None';
        }

        $.getJSON(json_url, function(data) {
            if (!data.error) {
                $('#trackInput_error').addClass('d-none');
                for (let field in data.fields) {
                    $('#appInfoModal').find(`[data-info="${field}"`).text(data.fields[field]);
                }
                $('#appInfoModal').modal();
            } else {
                $('#trackInput_error.d-none').text(data.error).removeClass('d-none');
            }
        });
    });

    $('.nice-select').on('mouseup', 'li', function() {
        let selected_option_val = $(this).data('value');
        let select_to_change = $(this).parent().parent().parent().find('select');
        select_to_change.find('option:selected').removeAttr('selected');
        select_to_change.find('option[value='+selected_option_val+']').attr('selected', 'selected')
    });

});