let button_1 = document.getElementById('button_Prod');
let type_account = document.getElementById('type_compte');
let button_Part = document.getElementById('button_Part');

button_1.addEventListener('click', (event) => {
    type_account.value = 'producteur';
});
button_Part.addEventListener('click', (event) => {
    type_account.value = 'particulier';
})
