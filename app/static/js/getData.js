// let obtenerFila = document.getElementById("fila1");

// let elementosFila = obtenerFila.getElementsByTagName("td")

// console.log(elementosFila);

// let tablaTrabajo = document.getElementById('tableWork');

// function mostrarFila(tabla, numeroFila){
//     let fila = tabla.rows[numeroFila].cells;
//     for (const celda of fila){
//         console.log(celda.innerHTML);
//     }
// }

// mostrarFila(tablaTrabajo, 1);

let tablaTrabajo = document.getElementById('tableWork');

function mostrarFila(tabla, numeroFila){
    let fila = tabla.rows[numeroFila].getElementsByTagName('td');
    for (const celda of fila){
        console.log(celda.innerHTML);
    }
}

mostrarFila(tablaTrabajo, 1);