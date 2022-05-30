package runner;

import cucumber.api.CucumberOptions;
import cucumber.api.testng.AbstractTestNGCucumberTests;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;
import pages.FlashMain;

import java.util.concurrent.TimeUnit;

@CucumberOptions(features = {"src/testjava/resources/FlashCreation.feature"}, glue = {"steps"})
public class TestNGRunner extends AbstractTestNGCucumberTests {

    public static WebDriver driver;
    public static FlashMain flashMain;

    @BeforeSuite
    public void setUp() {
        System.setProperty(
                "webdriver.chrome.driver",
                "C:/Users/patri/Documents/Coding/chromedriver.exe"
        );

        driver = new ChromeDriver();
        flashMain = new FlashMain(driver);

        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
    }

    @AfterSuite
    public void tearDown() {
        driver.quit();
    }


}
