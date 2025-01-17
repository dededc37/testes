var resultado = 0
var digitando = ''
var op_at = '+'

function digito(d) {
    digitando += d
}

function mais() {
    add(Number(digitando))
    digitando = ''
    op_at = '+'
}

function menos() {
    add(Number(digitando))
    digitando = ''
    op_at = '-'
}

function dividido() {
    add(Number(digitando))
    digitando = ''
    op_at = '/'
}

function vezes() {
    add(Number(digitando))
    digitando = ''
    op_at = '*'
}

function add(n) {
    switch (op_at) {
        case '+':
          resultado += n
          break
        case '-':
          resultado -= n
          break
        case '*':
          resultado *= n
          break
        case '/':
          resultado /= n
          break
    }
}

function igual() {
    add(Number(digitando))
    window.alert('A soma dos valores é igual a: ' + resultado)
    resultado = 0
    digitando = ''
    op_at = '+'
}