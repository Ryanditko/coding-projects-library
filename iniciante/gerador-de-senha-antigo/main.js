const letrasMaiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const letrasMinusculas = "abcdefghijklmnopqrstuvwxyz";
const numeros = "0123456789";
const simbolos = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~";

function GerarSenha(tamanho) {
    const caracteres = letrasMaiusculas + letrasMinusculas + numeros + simbolos;
    let senha = "";
    for (let i = 0; i < tamanho; i++) {
        const indice = Math.floor(Math.random() * caracteres.length);
        senha += caracteres[indice];
    }
    return senha;
}

console.log(GerarSenha(12));

