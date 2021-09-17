phrases = [
  { text: 'отправить другу смешную гифку', image: 'https://code.s3.yandex.net/web-code/procrastinate/1.gif' },
  { text: 'посмотреть скидки на авиабилеты', image: 'https://code.s3.yandex.net/web-code/procrastinate/2.png' },
  { text: 'разобраться, о чём поют рэперы', image: 'https://code.s3.yandex.net/web-code/procrastinate/3.png' },
  { text: 'Юрий Дудь', image: 'https://code.s3.yandex.net/web-code/procrastinate/4.png' },
  { text: 'расставить книги на полке по цвету', image: 'https://code.s3.yandex.net/web-code/procrastinate/5.png' },
  { text: 'читать про зарплаты в Сан-Франциско', image: 'https://code.s3.yandex.net/web-code/procrastinate/6.png' },
  { text: 'прочитать новости и ужаснуться в комментариях', image: 'https://code.s3.yandex.net/web-code/procrastinate/7.png' },
  { text: 'попасть в поток грустных песен и вспомнить все ошибки молодости', image: 'https://code.s3.yandex.net/web-code/procrastinate/8.png' },
  { text: 'посмотреть трейлер сериала и заодно первый сезон', image: 'https://code.s3.yandex.net/web-code/procrastinate/9.png' },
  { text: 'проверить непрочитанное в Telegram-каналах', image: 'https://code.s3.yandex.net/web-code/procrastinate/10.png' }
];


let button = document.querySelector('.button')
let phrase = document.querySelector('.phrase')
let advice = document.querySelector('.advice')
let image = document.querySelector('.image')


!function smoothly(t){
  const e=new 
  WeakMap,n=(t,e,n)=>new 
  Promise(o=>{
    const s=()=>{t.removeEventListener("transitionend",s),o()};
    t.style[e]=n, 
    t.addEventListener("transitionend",s)
  }), o=t=>n(t,"opacity",0), s=t=>n(t,"opacity",1),i=t=>(t=>new Promise(e=>setTimeout(e,t)))
  
  (1e3).then(()=>o(t)).then(()=>{const n=e.get(t);
  return t[n.prop]=n.contents.shift(),s(t)}).then(()=>e.get(t).contents.length?i(t):(t=>{e.get(t).timer=null})(t));

  t.smoothly=((t,n,r)=>{((t,n)=>{e.has(t)||(t.style.transition=n)})(t,"all 1s ease-in-out"),e.has(t)||e.set(t,{prop:n,contents:[],timer:null});
  
  const c=e.get(t);
  c.contents.push(r), c.timer||(c.timer=setTimeout(()=>{if(c.contents.length>1)return i(t);
  c.timer=null,(t=>o(t).then(()=>{const n=e.get(t);
  return t[n.prop]=n.contents.shift(),s(t)}))(t)},0))})
}(window);


function getRandomElement(arr) {
  let randIndex = Math.floor(Math.random() * arr.length);
  return arr[randIndex];
}


button.addEventListener('click', function () {
  let randomElement = getRandomElement(phrases);
  smoothly(phrase, 'textContent', randomElement.text);
  smoothly(image, 'src', randomElement.image);

  if (randomElement.text.length > 40) {
    advice.style.fontSize = '33px';
  } else {
    advice.style.fontSize = '42px';
  }
});


for (let i = 0; i <= 2; i += 1) {
  let randIndex = Math.floor(Math.random() * phrases.length);
  smoothly(phrase, 'textContent', phrases[randIndex].text);
  smoothly(image, 'src',  phrases[randIndex].image);
}
