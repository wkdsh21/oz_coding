//데이터베이스
const data = [
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티', price: '390,000' },
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠', price: '188,000' },
    { category: "신발", brand: 'Nike', product: '에어포스 1', price: '137,000' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' },
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티2', price: '390,000' },
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠2', price: '188,000' },
    { category: "신발", brand: 'Nike', product: '에어포스 12', price: '137,000' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링2', price: '29,000' },
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티3', price: '390,000' },
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠3', price: '188,000' },
    { category: "신발", brand: 'Nike', product: '에어포스 13', price: '137,000' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링3', price: '29,000' },
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티3', price: '390,000' },
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠3', price: '188,000' },
    { category: "신발", brand: 'Nike', product: '에어포스 13', price: '137,000' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링3', price: '29,000' },
];
const dataTable = document.getElementById('data-table');
// 초기화
data.forEach((item) => {
    const row = dataTable.insertRow();
    row.insertCell(0).innerHTML = item.category;
    row.insertCell(1).innerHTML = item.brand;
    row.insertCell(2).innerHTML = item.product;
    row.insertCell(3).innerHTML = item.price;
});

//카테고리 정렬 
let category=document.querySelector("#inlineFormSelectPref")
category.addEventListener('change', function() {
    const selectedValue = category.value;
    const dataTable = document.getElementById('data-table');
    //모두 제거후
    let count=dataTable.rows.length
    while(0<count){
        dataTable.deleteRow(count-1)
        count-=1
    }
    
    // 다시생성
    data.forEach((item) => {
        if(item.category==selectedValue || selectedValue=="전체"){
            console.log("dd")
            const row = dataTable.insertRow();
            row.insertCell(0).innerHTML = item.category;
            row.insertCell(1).innerHTML = item.brand;
            row.insertCell(2).innerHTML = item.product;
            row.insertCell(3).innerHTML = item.price;
        }
    });
});

//검색창 조회
let search = document.querySelector("#search_button")
let searchData = document.querySelector("#search")
search.addEventListener('click', function() {
    const selectedValue = category.value;
    const dataTable = document.getElementById('data-table');
    //모두 제거후
    let count=dataTable.rows.length
    while(0<count){
        dataTable.deleteRow(count-1)
        count-=1
    }

    //다시 생성
    data.forEach((item) => {
        if((item.category==selectedValue || selectedValue=="전체") && item.product.includes(searchData.value)){
            console.log("dd")
            const row = dataTable.insertRow();
            row.insertCell(0).innerHTML = item.category;
            row.insertCell(1).innerHTML = item.brand;
            row.insertCell(2).innerHTML = item.product;
            row.insertCell(3).innerHTML = item.price;
        }
    });
})

//시계
setInterval(() =>{
    let today = new Date();  
    let clock = document.querySelector("#clock")
    clock.textContent=`${today.getFullYear()}/${today.getMonth()}/${today.getDate()} ${today.getHours()} : ${today.getMinutes()} : ${today.getSeconds()}`
},100)

//다크모드 설정
let btn = document.querySelector("#flexSwitchCheckDefault")
let btnLabel = document.querySelector(".form-check-label")
btn.addEventListener("click",function(event){
    if(btn.checked){
        document.querySelector("#product").classList.add('dark-mode')
        document.querySelector("#product_table").classList.add('table-dark')
        btnLabel.textContent="다크모드 ON"
    }
    else{
        document.querySelector("#product").classList.remove('dark-mode')
        document.querySelector("#product_table").classList.remove('table-dark')
        btnLabel.textContent="다크모드 OFF"
    }
})


//페이지네이션
let nav = document.querySelector("#navmain")
nav.addEventListener('click', function(e) {
    if(e.target.matches('li')) return;
    console.log(e.target.textContent)


    // const dataTable = document.getElementById('data-table');
    // //모두 제거후
    // let count=dataTable.rows.length
    // while(0<count){
    //     dataTable.deleteRow(count-1)
    //     count-=1
    // }
    
    // // 다시생성
    // data.forEach((item) => {
    //     if(item.category==selectedValue || selectedValue=="전체"){
    //         console.log("dd")
    //         const row = dataTable.insertRow();
    //         row.insertCell(0).innerHTML = item.category;
    //         row.insertCell(1).innerHTML = item.brand;
    //         row.insertCell(2).innerHTML = item.product;
    //         row.insertCell(3).innerHTML = item.price;
    //     }
    // });
});