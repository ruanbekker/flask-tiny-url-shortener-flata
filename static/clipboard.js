function copyToClipboard() {
  var copyText = document.getElementById("URLInput");
  copyText.select();
  document.execCommand("Copy");
}
