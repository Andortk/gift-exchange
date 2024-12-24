const imageElement = document.getElementById('gift-image');
const nextButton = document.getElementById('next-button');
const cardContainer = document.querySelector('.card-container');
const imageFolder = 'images/'; // Assuming images are in a folder named 'images'
let imageFiles = [];
let remainingImages = [];
const hohohoSound = document.getElementById('hohoho-sound');

// Function to load image filenames (assuming they are named 1.jpg, 2.jpg, etc.)
async function loadImageFiles() {
    // This will need to be updated based on how the images are actually stored/named
    for (let i = 1; i <= 16; i++) { // Assuming a maximum of 5 images for now
        imageFiles.push(`${imageFolder}${i}.jpg`);
    }
    remainingImages = [...imageFiles];
}

function showNextImage() {
    if (remainingImages.length === 0) {
        imageElement.src = 'images/christmas.png';
        imageElement.alt = 'No more gifts!';
        return;
    }

    cardContainer.classList.add('animate');
    setTimeout(() => {
        const randomIndex = Math.floor(Math.random() * remainingImages.length);
        const selectedImage = remainingImages.splice(randomIndex, 1)[0];
        imageElement.src = selectedImage;
        imageElement.alt = 'Christmas Gift';
        cardContainer.classList.remove('animate');
    }, 1000); // Match the animation duration

    // Play the hohoho sound
    hohohoSound.play();
}

nextButton.addEventListener('click', showNextImage);

// Load initial images
loadImageFiles();
