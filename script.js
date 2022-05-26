// Function to load user details to pages when logged in
async function loadUser() {
  let getUsername = sessionStorage.getItem("creds");
  document.getElementById('user').innerHTML = getUsername;
  let getUserRole =sessionStorage.getItem('role')
  if (getUserRole === "Standard User") {
    document.getElementById("mySets").hidden = true
    document.getElementById("mySetsTable").hidden = true
    document.getElementById("mySetsSpan").style.display = 'none'
  }
}





// For login and registration page ------------
async function login() {
  let usernameGiven = document.getElementById('uName').value;
  let passwordGiven = document.getElementById('pWord').value;

  let userCanLogin = false;

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

  if (userCanLogin) {
    alert("Going to the home page...")
    window.location.href="homepg.html"
  }
  else alert("Credentials were invalid. Please try again.");
}

async function register() {
  let usernameGiven = document.getElementById('uName').value;
  let passwordGiven = document.getElementById('pWord').value;

  let userCanRegister = true;

  const userListURL = 'http://localhost:7000/users';
  const userListResponse = await fetch(userListURL);
  const userList = await userListResponse.json();

  for (let user of userList) {
    if (usernameGiven === user.username) userCanRegister = false;
  }

  if (!userCanRegister) alert("That username is taken. Please provide a different one.");
  // add the new user credentials to database
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
function getMySets(userId) {

}

function getSets() {

}

// For card viewer page -----------------------
function getUserResponse() {

}

function revealAnswer() {

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
  console.log(newDeck);

  if (newDeck) {
    alert(`Your new deck ${newDeck.deckName} has been added. Start putting in cards!`)
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
    deckID: sessionStorage.getItem("deckID")
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
  console.log(`Added to  ${document.getElementById('deckname').value} : `);
  console.log(newCard);

  // Clear card form fields after creating
  document.getElementById('question').value = null;
  document.getElementById('answer').value = null;
}
