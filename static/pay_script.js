const wrapper = document.querySelector('.wrapper')
const buttons = document.querySelector('.buttons')
const buttonsItems = document.querySelectorAll('.buttons-item')
const payForm = document.querySelector('.payment')
const back = document.querySelector('.back')
const index = location.href
const telegram = Telegram.WebApp.initData
const emailInput = document.querySelector('.email').lastElementChild

for (let i = 0; i < buttonsItems.length; i++) {
    buttonsItems[i].addEventListener('click', () => {
        const email = emailInput.value
        const regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        const checkEmail = regex.test(email)
        if (!checkEmail && email != '') {
            const descriptionText = document.querySelector('.description')
            const errorText = document.querySelector('.error')
            descriptionText.style.display = 'none'
            errorText.style.display = 'block'
            emailInput.value = ''
            return
        }

        const price = Number(buttonsItems[i].textContent.split(' ')[3].replace('р', ''))
        let seals = buttonsItems[i].textContent.split(' ')[0]
        let min = Math.ceil(10000);
        let max = Math.floor(1000);
        let random = Math.floor(Math.random() * (max - min)) + min
        let transactionId = 0
        if (isNaN(seals)) {
            seals = 'consultation'
            transactionId = Number(String(random) + '01')
        } else {
            switch (seals) {
                case '10':

                    transactionId = String(random) + '02'
                    break;

                case '50':
                    transactionId = String(random) + '03'
                    break;

                case '100':
                    transactionId = String(random) + '04'
                    break;
                default:
                    break;
            }
            transactionId = Number(transactionId)
            seals = Number(seals)
        }
        console.log(price)
        console.log(email)
        console.log(transactionId)
        const options = {
            account: 62590341,
            amount: price,
            email,
            transactionId: transactionId
        };
        buttons.style.display = 'none'
        payForm.style.display = 'block'

        const tg = window.Telegram.WebApp
        const id = tg.chat.id


        // const pay = document.querySelector('.pay')
        // pay.addEventListener('click', () => {
        //     // платёж не прошёл
        //     const failBlock = document.querySelector('.fail')
        //     failBlock.style.display = 'block'

        //     //платёж прошёл успешно
        //     // fetch('donate', {
        //     //     method: 'POST',
        //     //     headers: {
        //     //         'Content-Type': 'application/json'
        //     //     },
        //     //     body: JSON.stringify({
        //     //         id,
        //     //         seals
        //     //     })
        //     // }).then(() => tg.close())
        // })
        var assistant = new Assistant.Builder();

        // платёж прошёл успешно
        assistant.setOnSuccessCallback(function (operationId, transactionId) {
            fetch('donate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    id,
                    seals
                })
            }).then(() => tg.close())
        });

        // платёж не прошёл
        assistant.setOnFailCallback(function (operationId, transactionId) {
            const failBlock = document.querySelector('.fail')
            failBlock.style.display = 'block'
        });

        // платёж обрабатывается
        // assistant.setOnInProgressCallback(function (operationId, transactionId) {
        //     // todo: тоже можно что-нибудь придумать
        // });

        assistant.build(options, 'payment-form');
    })
}

if (back) {
    back.addEventListener('click', () => {
        location.reload();
    })
}

