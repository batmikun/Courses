function modifyTableCell(rowIndex, columnIndex, newText) {                                   
    const table = document.querySelector('#myTable');
    const previousCell = table.rows[rowIndex].cells[columnIndex].innerHTML;                                       
    const cell = table.rows[rowIndex].cells[columnIndex];                                         
    cell.innerHTML = newText;
  
    return previousCell;
  }

console.log(modifyTableCell(0, 1, 'Joe'));