phrases = [
  { text: 'отправить другу смешную гифку', image: '../static/images/gif.gif' },
  { text: 'посмотреть скидки на авиабилеты', image: '../static/images/tickets.png' },
  { text: 'разобраться, о чём поют рэперы', image: '../static/images/rapers.png' },
  { text: 'Юрий Дудь', image: '../static/images/dud.png' },
  { text: 'расставить книги на полке по цвету', image: '../static/images/books.png' },
  { text: 'читать про зарплаты в Сан-Франциско', image: '../static/images/SF.png' },
  { text: 'прочитать новости и ужаснуться в комментариях', image: '../static/images/news.png' },
  { text: 'попасть в поток грустных песен и вспомнить все ошибки молодости', image: '../static/images/songs.png' },
  { text: 'посмотреть трейлер сериала и заодно первый сезон', image: '../static/images/TV.png' },
  { text: 'проверить непрочитанное в Telegram-каналах', image: '../static/images/mail.png' }
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