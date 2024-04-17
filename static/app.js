// File Chooser function
function readURL(input) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
          $('.picture-placeholder').attr('src', e.target.result);
      }

      reader.readAsDataURL(input.files[0]);
  }
}

$("#picture").change(function(){
  readURL(this);
});

// Camera Capture function
var cameraPermission = false;
$('#take-picture').on('click', function() {
  if (!cameraPermission) {
    Webcam.set({
      // width: 250,
      // height: 250,
      // dest_width: 250,
      // dest_height: 250,
      // crop_width: 250,
      // crop_height: 250,
      // I don't know how to properly get the right size
      image_format: 'webp',
      flip_horiz: true,
    });

    // Attach camera here
    Webcam.attach('#video-stream-placeholder');

    cameraPermission = true;
  } else {
    Webcam.snap( function(data_uri) {
      document.querySelector('.picture-placeholder').src = data_uri;
    });
  }
});

// Close the camera
$('.modal').on('hidden.bs.modal', function() {
  Webcam.reset();
  $('.picture-placeholder').attr('src', '');
  cameraPermission = false;
});
