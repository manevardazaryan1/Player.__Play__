let now_playing = document.querySelector(".now-playing");
let track_art = document.querySelector(".track-art");
let track_name = document.querySelector(".track-name");
let track_artist = document.querySelector(".track-artist");

let playpause_btn = document.querySelector(".playpause-track");
let next_btn = document.querySelector(".next-track");
let prev_btn = document.querySelector(".prev-track");

let seek_slider = document.querySelector(".seek_slider");
let volume_slider = document.querySelector(".volume_slider");
let curr_time = document.querySelector(".current-time");
let total_duration = document.querySelector(".total-duration");

let track_index = 0;
let isPlaying = false;
let updateTimer;

// Create new path element
let curr_track = document.createElement('path');

// Define the tracks that have to be played
let track_list = [{"name": "Golden", "path": "path/Golden/golden.mp3", "image": "images/Golden/https___images.genius.com_45d822dc3d5485ae646546e50367cfc5.300x300x1.png", "artist": 62}, {"name": "Blinding Lights", "path": "path/Blinding Lights/Blinding_Lights.mp3", "image": "images/Blinding Lights/the_weeknd_blinding_lights_vid_2020_billboard_1548.jpg", "artist": 61}, {"name": "In Da Club", "path": "path/In Da Club/In_Da_Club.mp3", "image": "images/In Da Club/cad3c39d33f4414fc12192c62e06c16c.jpg", "artist": 60}, {"name": "I Say A Little Prayer", "path": "path/I Say A Little Prayer/I_Say_A_Little_Prayer.mp3", "image": "images/I Say A Little Prayer/sotd-aretha-franklin-I-say-a-little-prayer-compressor.jpg", "artist": 59}, {"name": "I Love You Baby", "path": "", "image": "", "artist": 58}, {"name": "Loca", "path": "path/Loca/Loca.mp3", "image": "images/Loca/04980a2eec2bb00f64d7abc23b86692e_large-342126.jpg", "artist": 57}, {"name": "Can't Help Falling In Love", "path": "", "image": "", "artist": 56}, {"name": "I'd Rather Go Blind", "path": "path/I'd Rather Go Blind/Id_Rather_Go_Blind.mp3", "image": "images/I'd Rather Go Blind/ETTA-JAMES-_-I_d-Rather-Go-Blind.jpg", "artist": 55}, {"name": "Love Don't Cost a Thing", "path": "path/Love Don't Cost a Thing/Love_Dont_Cost_a_Thing.mp3", "image": "images/Love Don't Cost a Thing/1280x720.jpg", "artist": 54}, {"name": "The Show Must Go On", "path": "path/The Show Must Go On/The_Show_Must_Go_On.mp3", "image": "images/The Show Must Go On/maxresdefault_1.jpg", "artist": 53}, {"name": "Toxic", "path": "path/Toxic/maxresdefault_2.jpg", "image": "", "artist": 52}, {"name": "7 rings", "path": "path/7 rings/7_rings.mp3", "image": "images/7 rings/Ariana_Grande_-_7_Rings.jpeg", "artist": 51}, {"name": "Woman", "path": "path/Woman/E4aUNQVXEAQGC48.jpg", "image": "", "artist": 49}, {"name": "Don't Start Now", "path": "path/Don't Start Now/Dont_Start_Now.mp3", "image": "images/Don't Start Now/maxresdefault.jpg", "artist": 49}, {"name": "Love in Portofino", "path": "path/Love in Portofino/Love_in_Portofino.mp3", "image": "images/Love in Portofino/002bd2a8.jpeg", "artist": 47}, {"name": "Change The World", "path": "path/Change The World/Change_The_World.mp3", "image": "images/Change The World/maxresdefault.jpg", "artist": 46}, {"name": "My Fathers Son", "path": "path/My Fathers Son/Joe_Cocker_-_My_Fathers_Son_....mp3", "image": "images/My Fathers Son/maxresdefault_1_1.jpg", "artist": 45}, {"name": "And You My Love", "path": "path/And You My Love/Chris_Rea__And_You_My_Love_.mp3", "image": "images/And You My Love/189-chris-rea-aubergejpg.jpg", "artist": 44}, {"name": "Cardigan", "path": "path/Cardigan/Taylor_Swift_-_cardigan_Official_Music_Video.mp3", "image": "images/Cardigan/Taylor-Swift-stars-react-to-folklore.jpg", "artist": 43}, {"name": "Super Freaky Girl", "path": "path/Super Freaky Girl/Super_Freaky_Girl.mp3", "image": "images/Super Freaky Girl/76ad304d54105ca8149a912c0d752920.jpg", "artist": 42}, {"name": "Thinking Out Loud", "path": "path/Thinking Out Loud/Ed_Sheeran_-_Thinking_Out_Loud_Official_Music_Video.mp3", "image": "images/Thinking Out Loud/Single.jpeg", "artist": 41}, {"name": "Stuck with U", "path": "path/Stuck with U/Ariana_Grande_Justin_Bieber_-_Stuck_with_U_Lyric_Video.mp3", "image": "images/Stuck with U/maxresdefault.jpg", "artist": 40}, {"name": "Stuck with U", "path": "path/Stuck with U/Ariana_Grande_Justin_Bieber_-_Stuck_with_U_Lyric_Video.mp3", "image": "images/Stuck with U/maxresdefault.jpg", "artist": 51}, {"name": "Calm Down", "path": "path/Calm Down/Rema_Selena_Gomez_-_Calm_Down_Official_Music_Video.mp3", "image": "images/Calm Down/maxresdefault.jpg", "artist": 39}, {"name": "One Dance", "path": "path/One Dance/Drake_-_One_Dance_Lyrics_ft._Wizkid__Kyla.mp3", "image": "images/One Dance/Drake_Views_mp3_download_320kbps_mp3-tub.blogspot.com.jpg", "artist": 38}, {"name": "24K Magic", "path": "path/24K Magic/Bruno_Mars_-_24K_Magic_Official_Music_Video.mp3", "image": "images/24K Magic/653677.jpg", "artist": 37}, {"name": "Cold Heart", "path": "path/Cold Heart/Elton_John_Dua_Lipa_-_Cold_Heart_PNAU_Remix_Official_Video.mp3", "image": "images/Cold Heart/ed02af2f2bce35751ff19a28935a73dc12_resize_1400x1400xxjpegxffffffxnoups_Drvcv5S.jpg", "artist": 36}, {"name": "Cold Heart", "path": "path/Cold Heart/Elton_John_Dua_Lipa_-_Cold_Heart_PNAU_Remix_Official_Video.mp3", "image": "images/Cold Heart/ed02af2f2bce35751ff19a28935a73dc12_resize_1400x1400xxjpegxffffffxnoups_Drvcv5S.jpg", "artist": 49}, {"name": "Imagine", "path": "path/Imagine/IMAGINE._Ultimate_Mix_2020_-_John_Lennon__The_Plastic_Ono_Band_with_the_Fl_eNAbVj0.mp3", "image": "images/Imagine/b50da373a2bbfc2203545663a7016c4d.jpg", "artist": 35}];

function random_bg_color() {

  // Get a number between 64 to 256 (for getting lighter colors)
  let red = Math.floor(Math.random() * 256) + 64;
  let green = Math.floor(Math.random() * 256) + 64;
  let blue = Math.floor(Math.random() * 256) + 64;

  // Construct a color withe the given values
  let bgColor = "rgb(" + red + "," + green + "," + blue + ")";

  // Set the background to that color
  document.body.style.background = bgColor;
}

function loadTrack(track_index) {
  clearInterval(updateTimer);
  resetValues();
  curr_track.src = track_list[track_index].path;
  curr_track.load();

  track_art.style.backgroundImage = "url(" + track_list[track_index].image + ")";
  track_name.textContent = track_list[track_index].name;
  track_artist.textContent = track_list[track_index].artist;
  now_playing.textContent = "PLAYING " + (track_index + 1) + " OF " + track_list.length;

  updateTimer = setInterval(seekUpdate, 1000);
  curr_track.addEventListener("ended", nextTrack);
  random_bg_color();
}

function resetValues() {
  curr_time.textContent = "00:00";
  total_duration.textContent = "00:00";
  seek_slider.value = 0;
}

// Load the first track in the tracklist
loadTrack(track_index);

function playpauseTrack() {
  if (!isPlaying) playTrack();
  else pauseTrack();
}

function playTrack() {
  curr_track.play();
  isPlaying = true;
  playpause_btn.innerHTML = '<i class="fa fa-pause-circle fa-5x"></i>';
}

function pauseTrack() {
  curr_track.pause();
  isPlaying = false;
  playpause_btn.innerHTML = '<i class="fa fa-play-circle fa-5x"></i>';;
}

function nextTrack() {
  if (track_index < track_list.length - 1)
    track_index += 1;
  else track_index = 0;
  loadTrack(track_index);
  playTrack();
}

function prevTrack() {
  if (track_index > 0)
    track_index -= 1;
  else track_index = track_list.length;
  loadTrack(track_index);
  playTrack();
}

function seekTo() {
  let seekto = curr_track.duration * (seek_slider.value / 100);
  curr_track.currentTime = seekto;
}

function setVolume() {
  curr_track.volume = volume_slider.value / 100;
}

function seekUpdate() {
  let seekPosition = 0;

  if (!isNaN(curr_track.duration)) {
    seekPosition = curr_track.currentTime * (100 / curr_track.duration);

    seek_slider.value = seekPosition;

    let currentMinutes = Math.floor(curr_track.currentTime / 60);
    let currentSeconds = Math.floor(curr_track.currentTime - currentMinutes * 60);
    let durationMinutes = Math.floor(curr_track.duration / 60);
    let durationSeconds = Math.floor(curr_track.duration - durationMinutes * 60);

    if (currentSeconds < 10) { currentSeconds = "0" + currentSeconds; }
    if (durationSeconds < 10) { durationSeconds = "0" + durationSeconds; }
    if (currentMinutes < 10) { currentMinutes = "0" + currentMinutes; }
    if (durationMinutes < 10) { durationMinutes = "0" + durationMinutes; }

    curr_time.textContent = currentMinutes + ":" + currentSeconds;
    total_duration.textContent = durationMinutes + ":" + durationSeconds;
  }
}