// Function to load user details to pages when logged in
async function loadUser() {
  let getUsername = sessionStorage.getItem("creds");
  document.getElementById('user').innerHTML = getUsername;
  let getUserRole =sessionStorage.getItem('role')
  if (getUserRole === "Standard User") {
    document.getElementById("mySets").hidden = true
    document.getElementById("mySetsSpan").style.display = 'none'
   }
}

function loadForHomePage() {
  loadUser();

  getDecks();
}

async function loadDeckBrowsing() {
  loadUser();

  let getDeckBrowsing = sessionStorage.getItem("deckBrowsing");

  const questionElement = document.createElement('span');
  const answerElement = document.createElement('span');

  const getDeckURL = 'http://localhost:5000/cards/decks/' + getDeckBrowsing;
  const getDeckResponse = await fetch(getDeckURL);
  if (getDeckResponse.status === 200) {
    const deck = await getDeckResponse.json();

    questionElement.textContent = deck[0].question;
    answerElement.textContent = deck[0].answer;

    const questionBlock = document.getElementById('flipCardQuestion');
    questionBlock.appendChild(questionElement);
    const answerBlock = document.getElementById('flipCardAnswer');
    answerBlock.appendChild(answerElement);

    let copy = deck.slice(1);
    let iterate = copy[Symbol.iterator]();
    document.getElementById("nextQuestion").onclick = function() {
      let next = iterate.next()
      if (next.done) {alert("No more cards in the deck; you're finished!")}
      else {
        console.log(next.value.question)
        questionBlock.innerText = next.value.question
        revealAnswer()

        answerBlock.innerText = next.value.answer
      }
    };
  }
  else alert("There was an error in obtaining cards from this deck. Try again later.");


}



// For login and registration page ------------
async function login() {
  // Gather credentials entered in username and password fields
  let usernameGiven = document.getElementById('uName').value;
  let passwordGiven = document.getElementById('pWord').value;

  let userCanLogin = false;

  // GET all users from database for verification loop
  const userListURL = 'http://localhost:7000/users';
  const userListResponse = await fetch(userListURL);
  const userList = await userListResponse.json();

  // Loop through the list and verify the right user
  for (let user in userList) {
    if (usernameGiven === userList[user].username && passwordGiven === userList[user].password) {
      userCanLogin = true;
      console.log("Welcome back, " + userList[user].username);
      sessionStorage.setItem("creds", userList[user].username);
      sessionStorage.setItem("role", userList[user].userRole);
      sessionStorage.setItem("userID", userList[user].userId);
      break;
    }
  }

  // Proceed to home page if the user is set to login, otherwise alert them of bad username/password
  if (userCanLogin) {
    alert("Going to the home page...")
    window.location.href="homepage.html"
  }
  else alert("Credentials were invalid. Please try again.");
}

async function register() {
  // Gather credentials entered in username and password fields
  let usernameGiven = document.getElementById('uName').value;
  let passwordGiven = document.getElementById('pWord').value;

  let userCanRegister = true;

  // GET all users from database for verification loop
  const userListURL = 'http://localhost:7000/users';
  const userListResponse = await fetch(userListURL);
  const userList = await userListResponse.json();

  // Check to see if the credentials match a user
  for (let user of userList) {
    if (usernameGiven === user.username) userCanRegister = false;
  }

  // Proceed if the username exists, otherwise tell the user the given username already exists
  if (!userCanRegister) alert("That username is taken. Please provide a different one.");
  else {
    const createUserData = {
      username: usernameGiven,
      password: passwordGiven,
      userRole: "Standard User"
    };
    const createUserOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(createUserData)
    };
    const createUserResponse = await fetch(userListURL, createUserOptions);
    const newUser = await createUserResponse.json();
    console.log(newUser);

    alert("Registration complete!");
    login();
  }
}

// For home page ------------------------------
async function getDecks() {
  // Load all decks
  const deckListURL = 'http://localhost:5000/decks';
  const deckListResponse = await fetch(deckListURL);
  const deckList = await deckListResponse.json();

  // Load a random number of decks that a standard user can choose from
  // Then add each deck to table with a link to the deck page
  let decks = [];
  console.log(deckList.length);
  for (let i = 0; i < deckList.length; i++) {
    decks.push(deckList[i]);

    const outerElement = document.createElement('tr');
    const innerElement = document.createElement('td');
    const elmnt = document.createElement('a');


    innerElement.setAttribute('class', 'deckinfo');
    elmnt.setAttribute('id', 'deckLink');
    elmnt.setAttribute('href', 'flashpoint-test.html'); // Change this later

    let deckName = decks[i].deckName;
    console.log(deckName);
    elmnt.textContent = deckName;

    //console.log(innerElement);
    //const deckTable = document.querySelectorAll(".deckinfo");
    const parent = document.getElementById("parent");
    parent.appendChild(outerElement);
    outerElement.appendChild(innerElement);
    innerElement.appendChild(elmnt);
    //console.log(outerElement);

    elmnt.addEventListener("click", event => {
      sessionStorage.setItem("deckBrowsing", decks[i].deckId);
    });
  }
}

// For card viewer page -----------------------
function getUserResponse() {
  var card = document.querySelector('.flip-card-inner');
  card.classList.toggle('animation');
  document.getElementById('AnswerSubmit').disabled = true
  document.getElementById('nextQuestion').disabled = false
}

function revealAnswer() {
  var card = document.querySelector('.flip-card-inner');
  card.classList.toggle('animation');
  document.getElementById('AnswerSubmit').disabled = false
  document.getElementById('nextQuestion').disabled = true

  document.getElementById('cardAnswer').value = null
}

function sortCardsInDeck() {

}

// For card/set creator/editor page -----------
async function createNewDeck() {
  // Gather details for new deck
  let newDeckDetails = {
    deckId: document.getElementById("deckid").value,
    userId: sessionStorage.getItem("userID"),
    deckName: document.getElementById("deckname").value
  };

  // Send details to server and create new deck
  const newDeckURL = 'http://localhost:5000/decks';
  const newDeckOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newDeckDetails)
  };
  const newDeckResponse = await fetch(newDeckURL, newDeckOptions);
  const newDeck = await newDeckResponse.json();

  if (newDeck) {
    const messageBox = document.getElementById('newDeckFeedback');
    messageBox.innerHTML = "New deck created! You may now create cards for this new deck.";
    sessionStorage.setItem("deckID", newDeck.deckId)
  }



  // Disable deck fields after creating new deck
  document.getElementById('questionForm').hidden = false;
  document.getElementById('deckid').disabled = true;
  document.getElementById('deckname').disabled = true;
  document.getElementById('decksubmit').disabled = true;
}

async function addNewCard() {
  // Place card details into an object that will be parsed to JSON
  let newCardDetails = {
    question: document.getElementById('question').value,
    answer: document.getElementById('answer').value,
    deckId: sessionStorage.getItem("deckID")
  };

  // Send new card info to server and add to database
  const newCardURL = 'http://localhost:5000/cards';
  const newCardOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newCardDetails)
  };
  const newCardResponse = await fetch(newCardURL, newCardOptions);
  const newCard = await newCardResponse.json();

  // Display message below button indicating that the card was added successfully
  const messageBox = document.getElementById('newCardFeedback');
  messageBox.innerHTML = "Card successfully added to the deck!";

  // Clear card form fields after creating
  document.getElementById('question').value = null;
  document.getElementById('answer').value = null;
}
