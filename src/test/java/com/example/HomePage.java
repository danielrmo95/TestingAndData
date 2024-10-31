package com.example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class HomePage {

    private WebDriver driver;
    private WebDriverWait wait;

    // Elementos
    private By originField = By.xpath("//label[contains(text(), 'Origen')]/following-sibling::div//input[@class='input-tag']");
    private By destinationField = By.xpath("//label[contains(text(), 'Destino')]/following-sibling::div//input[@class='input-tag']");
    private By searchButton = By.xpath("//button[./em[text()='Buscar']]"); 
    private By dateField = By.xpath("//label[contains(text(), 'Fechas')]/following-sibling::div//input[@class='input-tag']");
    private By datein = By.xpath("//div[contains(@class, 'sbox5-monthgrid-datenumber') and .//div[text()='15']]");
    private By datefi = By.xpath("//div[contains(@class, 'sbox5-monthgrid-datenumber') and .//div[text()='16']]");

    // Constructor
    public HomePage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(20)); // 10 segundos de espera
    }

    // Métodos de la página
    public void setOrigin(String origin) {
        WebElement element = wait.until(ExpectedConditions.visibilityOfElementLocated(originField));
        element.sendKeys(origin);
    }

    public void setDestination(String destination) {
        WebElement element = wait.until(ExpectedConditions.elementToBeClickable(destinationField));
        element.click();
        wait.until(ExpectedConditions.visibilityOfElementLocated(destinationField)).sendKeys(destination);
    }

    public void selectDates() {
        WebElement dateFieldElement = wait.until(ExpectedConditions.elementToBeClickable(dateField));
        dateFieldElement.click();
        WebElement dateInElement = wait.until(ExpectedConditions.elementToBeClickable(datein));
        dateInElement.click();
        WebElement dateFiElement = wait.until(ExpectedConditions.elementToBeClickable(datefi));
        dateFiElement.click();
    }

    public void clickSearchButton() {
        WebElement button = wait.until(ExpectedConditions.elementToBeClickable(searchButton));
        button.click();
    }
}
