package steps;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import org.openqa.selenium.WebDriver;
import org.testng.Assert;
import pages.FlashMain;
import runner.TestNGRunner;


public class FlashStepCreateImpl {

    public static WebDriver driver = TestNGRunner.driver;
    public static FlashMain flashMain = TestNGRunner.flashMain;

    @Given("^The User is on the login page$")
    public void the_User_is_on_the_login_page() {
        driver.get(
        "C:/Users/patri/Documents/Coding/RevTraining/Python/Flashpoint/FlashpointApp/flashFront/login-register.html"
        );
    }

    @When("^The User enters flash_user into the username input$")
    public void the_User_enters_flash_user_into_the_username_input() {
        flashMain.enterUsername();
    }

    @When("^The User enters pwd1 into the password input$")
    public void the_User_enters_pwd1_into_the_password_input() {
        flashMain.enterPassword();
    }

    @When("^The User clicks on the login button$")
    public void the_User_clicks_on_the_login_button() {
        flashMain.pressLoginBtn();
    }

    @When("^The User is on the home page$")
    public void the_User_is_on_the_home_page() {
        Assert.assertEquals(driver.getTitle(), "User Home Page");
    }

    @When("^The User clicks on the option to create a new deck$")
    public void the_User_clicks_on_the_option_to_create_a_new_deck() {
        flashMain.pressNewDeckBtn();
    }

    @When("^The User types 50 into the id input$")
    public void the_User_types_50_into_the_id_input() {
        flashMain.enterIdInput();
    }

    @When("^The User enters basketball into the deck name input$")
    public void the_User_enters_basketball_into_the_deck_name_input() {
        flashMain.enterDeckNameInput();
    }

    @When("^The User clicks the submit deck button$")
    public void the_User_clicks_the_submit_deck_button() {
        flashMain.pressSubmitDeckBtn();
    }

    @When("^The User enters who was the 2022 NBA MVP into the question input$")
    public void the_User_enters_who_was_the_2022_NBA_MVP_into_the_question_input() {
        flashMain.enterQuestionInput();
    }

    @When("^The User enters Nikola Jokic into the answer input$")
    public void the_User_enters_Nikola_Jokic_into_the_answer_input() {
        flashMain.enterAnswerInput();
    }

    @When("^The User clicks the submit card button$")
    public void the_User_clicks_the_submit_card_button() {
        flashMain.pressSubmitCardBtn();
    }

    @Then("^The creation message should be <message>$")
    public void the_creation_message_should_be_() {
        Assert.assertEquals()
    }

}
