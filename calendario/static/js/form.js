$(document).ready(function () {
    // Função a ser executada quando o documento estiver pronto
    function validarNome() {
        let nome = $("#nome").val();
        var regex = /^[a-zA-Z]+$/;

        if (!regex.test(nome)) {
            $("#errorNome").css({
                "display": "block"
            });
            return false
        } else {
            $("#errorNome").css({
                "display": "none"
            });
            return true
        }
    };
    function validarSobrenome() { 
        let nome = $("#sobrenome").val();
        var regex = /^[a-zA-Z]+$/;

        if (!regex.test(nome)) {
            $("#errorSobreNome").css({
                "display": "block"
            });
            return false
        } else {
            $("#errorSobreNome").css({
                "display": "none"
            });
            return true
        }
    };
    function validarUsername() {
        let username = $("#username").val();
        var regex = /^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]*$/;
        var numLetras = (username.match(/[a-zA-Z]/g) || []).length;


        if (!regex.test(username) || numLetras < 3) {
            $("#errorUsername").css({
                "display": "block"
            });
            return false
        } else {
            $("#errorUsername").css({
                "display": "none"
            });
            return true
        }
    };
    function validarEmail() {
        let email = $("#email").val();
        var regex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;


        if (!regex.test(email)) {
            $("#erroremail").css({
                "display": "block"
            });
            return false
        } else {
            $("#erroremail").css({
                "display": "none"
            });
            return true
        }
    };
    function validarSenha() {
        var senha = $("#senha").val();
        var regexLetrasNumeros = /^(?=.*[a-zA-Z])(?=.*\d)[A-Za-z\d]{6,}$/;
        var regexEspaco = /\s/;

        if (!regexLetrasNumeros.test(senha) || regexEspaco.test(senha)) {
            $("#errorSenha").css("display", "block");
            return false
        } else {
            $("#errorSenha").css("display", "none");
            return true
        }
    };
    function validarConfirmarsenha() {
        var senha = $("#confirmarSenha").val();
        var regexLetrasNumeros = /^(?=.*[a-zA-Z])(?=.*\d)[A-Za-z\d]{6,}$/;
        var regexEspaco = /\s/;

        if (!regexLetrasNumeros.test(senha) || regexEspaco.test(senha)) {
            $("#errorConfirmarSenha").css("display", "block");
            return false
        } else {
            $("#errorConfirmarSenha").css("display", "none");
            return true
        }
    };
    function validarForm(){
        let nomeValido = validarNome();
        let sobrenomeValido = validarSobrenome();
        let usernameValido = validarUsername();
        let emailValido = validarEmail();
        let senhaValida = validarSenha();
        let confirmarSenhaValida = validarConfirmarSenha();

        if (nomeValido && sobrenomeValido && usernameValido && emailValido && senhaValida && confirmarSenhaValida) {
            return true;
        } else {
            $("#errorMensagem").css("display", "block");
            return false;
        }
    }

    $("#nome").on("input", validarNome())
    $("#sobrenome").on("input", validarSobrenome())
    $("#username").on("input", validarUsername())
    $("#email").on("input", validarEmail())
    $("#senha").on("input", validarSenha())
    $("#confirmarSenha").on("input", validarConfirmarsenha())
    $("#meuForm").submit(function (event) {
        if (!validarForm()) {
            event.preventDefault();
        }
    });

});
