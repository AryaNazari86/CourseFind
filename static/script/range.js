var elem = document.getElementById("maxPrice");

var rangeValue = function(){
  var newValue = elem.value;
  var target = document.getElementById("maxPriceValue");
  target.innerHTML = PersianTools.digitsEnToFa(PersianTools.addCommas(newValue)) + " تومان";
}

elem.addEventListener("input", rangeValue);