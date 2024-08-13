package com.example;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class HomePageTest {

    private WebDriver driver;
    private HomePage homePage;

    @BeforeEach
    public void setUp() {
        WebDriverManager.chromedriver().setup();
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");
        options.addArguments("user-data-dir=C:\\Users\\Daniel Romero\\Desktop\\fastapi-mysql-restapi\\User Data");
        options.addArguments("profile-directory=Default");
        options.addArguments("--incognito");
        options.addArguments("--disable-cache");

        driver = new ChromeDriver(options);
        homePage = new HomePage(driver);
    }

    @Test
    public void testFlightSearch() throws InterruptedException {
        driver.get("https://www.despegar.com.co/");

        homePage.setOrigin("Bogotá, Bogotá D.C., Colombia");
        homePage.setDestination("San");
        WebElement firstItem = driver.findElement(By.cssSelector("li.item.-active"));
        firstItem.click();
        homePage.selectDates();

        homePage.clickSearchButton();

    }

    @AfterEach
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
