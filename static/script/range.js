var elem = document.getElementById("maxPrice");

var rangeValue = function(){
  let newValue = elem.value;
  let target = document.getElementById("maxPriceValue");
  target.innerHTML = PersianTools.digitsEnToFa(PersianTools.addCommas(newValue)) + " تومان";
}

elem.addEventListener("input", rangeValue);

var elemMobile = document.getElementById("maxPrice-mobile");

var rangeValueMobile = function(){
  let newValue = elemMobile.value;
  let target = document.getElementById("maxPriceValue-mobile");
  target.innerHTML = PersianTools.digitsEnToFa(PersianTools.addCommas(newValue)) + " تومان";
}

elemMobile.addEventListener("input", rangeValueMobile);