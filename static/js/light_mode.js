function lightMode() {  
    let text = document.querySelector('.mode')

    if (text.innerHTML == 'Light Mode') {
        text.innerHTML = 'Dark Mode'
        text.className = 'mode dark'
        document.body.style.backgroundColor = '#fff'
        document.body.style.color = '#000'
    }else {
        text.innerHTML = 'Light Mode'  
        text.className = 'mode light'
        document.body.style.backgroundColor = '#101010'
        document.body.style.color = '#fefefe'
    }
    
}