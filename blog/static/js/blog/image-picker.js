(function () {

    function readURL(input, preview) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function(e) {
                preview.setAttribute('style', "background-image: url('" + e.target.result + "')");
            }

            reader.readAsDataURL(input.files[0]); // convert to base64 string
        }
        else {
            preview.removeAttribute('style');
        }
    }

    var imagePickers = document.getElementsByClassName('image-picker');
    for (var i = 0; i < imagePickers.length; i++) {
        var
            picker = imagePickers[i],
            inp = picker.getElementsByTagName('input')[0],
            preview = picker.getElementsByClassName('image-picker-preview')[0],
            previewClose = preview.getElementsByClassName('close')[0]
        ;

        if (!!previewClose) {
            previewClose.onclick = function (e) {
                inp.value = '';
                readURL(inp, preview);
            }
        }

        if (!!inp) {
            inp.onchange = function (e) {
                readURL(inp, preview);
            }
        }

        // Инициализация при обновлении
        if (!!inp && !!preview ) {
            readURL(inp, preview);
        }
    }

})()