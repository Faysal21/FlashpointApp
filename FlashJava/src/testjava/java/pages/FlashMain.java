package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class FlashMain {

    // Find elements-----------------------------------------------------------------
    @FindBy(id="uName")
    private WebElement username_input;

    @FindBy(id="pWord")
    private WebElement password_input;

    @FindBy(xpath="/html/body/div/input[3]")
    private WebElement login_btn;

    @FindBy(xpath="/html/body/div[1]/button[1]")
    private WebElement create_new_deck_btn;

    @FindBy(id="deckid")
    private WebElement deck_id_input;

    @FindBy(id="deckname")
    private WebElement deck_name_input;

    @FindBy(id="decksubmit")
    private WebElement submit_deck_btn;

    @FindBy(id="question")
    private WebElement new_question_input;

    @FindBy(id="answer")
    private WebElement new_answer_input;

    @FindBy(xpath="")
    private WebElement submit_card_btn;

    public FlashMain(WebDriver driver) {
        PageFactory.initElements(driver, this);
    }

    // Create Actions For Elements-------------------------------------------------------------

    public void enterUsername() {
        username_input.sendKeys("flash_user");
    }

    public void enterPassword() {
        password_input.sendKeys("pwd1");
    }

    public void pressLoginBtn() {
        login_btn.click();
    }

    public void pressNewDeckBtn() {
        create_new_deck_btn.click();
    }

    public void enterIdInput() {
        deck_id_input.sendKeys("50");
    }

    public void enterDeckNameInput() {
        deck_name_input.sendKeys("basketball");
    }

    public void pressSubmitDeckBtn() {
        submit_deck_btn.click();
    }

    public void enterQuestionInput() {
        new_question_input.sendKeys("Who was the 2022 NBA MVP?");
    }

    public void enterAnswerInput() {
        new_answer_input.sendKeys("Nikola Jokic");
    }

    public void pressSubmitCardBtn() {
        submit_card_btn.click();
    }

}
