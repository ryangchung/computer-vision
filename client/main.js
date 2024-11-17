// // import "./style.css";
// // import javascriptLogo from './javascript.svg'
// // import viteLogo from '/vite.svg'
// // import { setupCounter } from './counter.js'

// // document.querySelector('#app').innerHTML = `
// //   <div>
// //     <a href="https://vite.dev" target="_blank">
// //       <img src="${viteLogo}" class="logo" alt="Vite logo" />
// //     </a>
// //     <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
// //       <img src="${javascriptLogo}" class="logo vanilla" alt="JavaScript logo" />
// //     </a>
// //     <h1>Hello Vite!</h1>
// //     <div class="card">
// //       <button id="counter" type="button"></button>
// //     </div>
// //     <p class="read-the-docs">
// //       Click on the Vite logo to learn more
// //     </p>
// //   </div>
// // `

// // setupCounter(document.querySelector('#counter'))

// //When upload


// document.getElementById("upload-btn").addEventListener("click", async (e) => {

//     e.preventDefault()
  
//     const input = document.getElementById("upload-input");
//     const resultElement = document.getElementById("result");
  
//     // Check if an image is selected
//     if (input.files.length === 0) {
//       console.log("No file selected.");
//       resultElement.textContent = "Please select an image file.";
//       return;
//     }
  
//     const formData = new FormData();
//     formData.append("file", input.files[0]);
  
//     try {
//         const response = await fetch("http://127.0.0.1:8000/predict", {
//           method: "POST",
//           body: formData,
//         });
      
//         const data = await response.json();
      
//         if (data.error) {
//           throw new Error(data.error);
//         }
      
//         const result = data.productive ? "Productive" : "Unproductive";

//         if (result == "Productive") {
//             document.getElementById('verify').textContent = "Website Allowed!";

//         }
//         resultElement.textContent = `Result: ${result}`;

       

        
//       } catch (error) {
//         console.error("Error:", error);
//         resultElement.textContent = `An error occurred: ${error.message}`;

       

        
//     }

//     setTimeout(() => {
//         if (resultElement) {
//           resultElement.textContent = "";
//         }
//       }, 100000); // Clear result after 5 seconds
//   });
  