//let nome= prompt("Como você se chama?")

//if (nome == null) {
  //  alert("Recarregue a página")
//} else {
    //let correto = confirm("Você se chama " + nome + "?")
//if (correto) {
   // alert(nome + " Bem vindo ao site de cursos")
//} else
   // alert("Recague a página")
//}

//document.addEventListener("DOMContentLoaded", function (){
   // const formLogin = document.getElementById('form-login')
   // formLogin.addEventListener("submit", function (event){
     //   const inputEmail = document.getElementById('input-email')
       // const inputSenha = document.getElementById('input-senha')
       // let temErro = False
        //verificar se os input estão vazios

     //   if (inputEmail.value === '') {
         //   inputEmail.classList.add('is-invalid')
         //   temErro = true
     //   } else {
       //     inputEmail.classList.remove('is-invalid')
      //  }

      //  if (inputSenha.value === '') {
      //      inputSenha.classList.add('is-invalid')
     //       temErro = true
     //   } else {
       //     inputSenha.classList.remove('is-invalid')
     //   }

      //  if (temErro){
            //evita de enviar o formulario
   //         event.preventDefault()
    //        alert("Preencha todos os campos")
     //   }
//    })
//})

function limpaInputslogin(){
    const inputEmail = document.getElementById('input_email')
    const inputSenha = document.getElementById('input_senha')

    inputEmail.value = ''
    inputSenha.value = ''

}

function limpaInputsCadastroFuncionario() {
    const inputNomeFuncionario = document.getElementById("input_nome")
    const inputDatadeNascimento = document.getElementById("input_data")
    const inputCPF = document.getElementById("input_cpf")
    const inputEmail = document.getElementById("input_email")
    const inputSenha = document.getElementById("input_senha")
    const inputCargo = document.getElementById("input_cargo")
    const inputSalario = document.getElementById("input_salario")


    inputNomeFuncionario.value = ""
    inputDatadeNascimento.value = ""
    inputCPF.value = ""
    inputEmail.value = ""
    inputSenha.value = ""
    inputCargo.value = ""
    inputSalario.value = ""

}


document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.getElementById("form_login")

    formLogin.addEventListener("submit", function (event) {
        // Pegar os dois inputs do formulario
        const inputEmail = document.getElementById("input_email")
        const inputSenha = document.getElementById("input_senha")

        let temErro = false

        // Verificar se os inputs estão vazios

        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }


        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

    })


    const formCadastroFuncionario = document.getElementById("form_cadastro_funcionario")


    formCadastroFuncionario.addEventListener("submit", function (event) {
        const inputNomeFuncionario = document.getElementById("input_nome")
        const inputDatadeNascimento = document.getElementById("input_data")
        const inputCPF = document.getElementById("input_cpf")
        const inputEmail = document.getElementById("input_email")
        const inputSenha = document.getElementById("input_senha")
        const inputCargo = document.getElementById("input_cargo")
        const inputSalario = document.getElementById("input_salario")

        let temErro = false


        if (inputNomeFuncionario.value === '') {
            inputNomeFuncionario.classList.add('is-invalid')
            temErro = true
        } else {
            inputNomeFuncionario.classList.remove('is-invalid')
        }


        if (inputDatadeNascimento.value === '') {
            inputDatadeNascimento.classList.add('is-invalid')
            temErro = true
        } else {
            inputDatadeNascimento.classList.remove('is-invalid')
        }


        if (inputCPF.value === '') {
            inputCPF.classList.add('is-invalid')
            temErro = true
        } else {
            inputCPF.classList.remove('is-invalid')
        }


        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }


        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }


        if (inputCargo.value === '') {
            inputCargo.classList.add('is-invalid')
            temErro = true
        } else {
            inputCargo.classList.remove('is-invalid')
        }

        if (inputSalario.value === '') {
            inputSalario.classList.add('is-invalid')
            temErro = true
        } else {
            inputSalario.classList.remove('is-invalid')
        }


        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

    })


})
