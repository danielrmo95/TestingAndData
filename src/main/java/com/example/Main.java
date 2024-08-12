package com.example;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class Main {
    public static void main(String[] args) {
        // Configura WebDriverManager para Chrome
        WebDriverManager.chromedriver().setup();

        // Configura opciones de Chrome
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");
        // Opcional: Usa el perfil de usuario si es necesario
        options.addArguments("user-data-dir=C:\\Users\\Daniel Romero\\Desktop\\fastapi-mysql-restapi\\User Data");
        options.addArguments("profile-directory=Default");

        // Inicializa el navegador con las opciones configuradas
        WebDriver driver = new ChromeDriver(options);

        try {
            driver.get("https://www.despegar.com.co/");

            // Imput origen - destino

            WebElement originField = driver.findElement(By.xpath("//label[contains(text(), 'Origen')]/following-sibling::div//input[@class='input-tag']"));
            WebElement destinationField = driver.findElement(By.xpath("//label[contains(text(), 'Destino')]/following-sibling::div//input[@class='input-tag']"));
            
            originField.sendKeys("Bogotá, Bogotá D.C., Colombia");
            Thread.sleep(2000); 
            destinationField.sendKeys("Santa Marta, Magdalena, Colombia");
            Thread.sleep(5000); 


            // Dates
            WebElement dateField = driver.findElement(By.xpath("//label[contains(text(), 'Fechas')]/following-sibling::div//input[@class='input-tag']"));
            dateField.click();
            Thread.sleep(2000); 
            WebElement datein = driver.findElement(By.xpath("//div[contains(@class, 'sbox5-monthgrid-datenumber') and .//div[text()='15']]"));
            datein.click();
            Thread.sleep(2000); 
            WebElement datefi = driver.findElement(By.xpath("//div[contains(@class, 'sbox5-monthgrid-datenumber') and .//div[text()='16']]"));
            datefi.click();

            WebElement searchButton = driver.findElement(By.xpath("//button[./em[text()='Buscar']]"));
            searchButton.click();


        } catch (Exception e) {
            e.printStackTrace();
        } 
    }
}