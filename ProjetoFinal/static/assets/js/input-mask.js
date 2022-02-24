// Example starter JavaScript for disabling form submissions if there are invalid fields
(function() {
    'use strict';
    window.addEventListener('load', function() {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

//Permite conversão de Number para Decimal no campo Altura

function setTwoNumberDecimal(event) {
    this.value = parseFloat(this.value).toFixed(2);
}

//Mascara para formatação do Telefone

const telefone = document.getElementById('telefone') // Seletor do campo de telefone

telefone.addEventListener('keypress', (e) => mascaraTelefone(e.target.value)) // Dispara quando digitado no campo
telefone.addEventListener('change', (e) => mascaraTelefone(e.target.value)) // Dispara quando autocompletado o campo

const mascaraTelefone = (valor) => {
    valor = valor.replace(/\D/g, "")
    valor = valor.replace(/^(\d{2})(\d)/g, "($1) $2")
    valor = valor.replace(/(\d)(\d{4})$/, "$1-$2")
    telefone.value = valor // Insere o(s) valor(es) no campo
}

//Retira os espaços e carecteres especiais no campo Nome e Sobrenome

var username = document.getElementById('username')
var nome_sobrenome = document.getElementsByClassName('nome_sobrenome')

$(username).keypress(function(e) {
    if (!/^[0-9a-zA-Z\-_.!@#&]+$/.test(String.fromCharCode(e.which)))
        return false;
});

$(nome_sobrenome).keypress(function(e) {
    if (!/^[a-zA-Z ]+$/.test(String.fromCharCode(e.which)))
        return false;
});