document.addEventListener('DOMContentLoaded', () => {
    const answerButton = document.querySelector('.answer')
    const tg = window.Telegram.WebApp
    const admId = tg.chat.id
    let user_id = ''
    fetch('queries', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ adm_id:admId })
    }).then(res => res.json())
        .then(res => {
            const queries = document.querySelector('.wrapper')
            if (res.status != 'denied') {
                const select = document.querySelector('.js-choice');
                const queries = res.queries
                for (let i = 0; i < queries.length; i++) {
                    let newOption = `<option value=${queries[i].user_id}>${queries[i].user_id}</option>`
                    select.innerHTML = newOption + select.innerHTML
                }
                const selectWithSearch = new Choices(select);
                const question = document.querySelector('.question')
                select.addEventListener('change', e => {
                    const value = e.target.value
                    user_id = value
                    for (let i = 0; i < queries.length; i++) {
                        if (queries[i].user_id == value) {
                            question.innerHTML = question.innerHTML + queries[i].question
                            answerButton.style.display = 'block'
                            break
                        }
                    }
                })
            } else {
                queries.innerHTML = 'доступ закрыт'
            }
        })
    answerButton.addEventListener('click', () => {
        fetch('queries', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                adm_id:admId, 
                user_id
            })
        }).then(() => tg.close())
    })
    
})