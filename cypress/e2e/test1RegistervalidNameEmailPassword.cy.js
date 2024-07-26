describe('User Registration', () => {
  it('should register a user with valid name, email, and password', () => {
    cy.visit('https://test-qa.inlaze.com/auth/sign-up');    
    cy.get('#full-name').type('Daniel Fernando Romero Ochoa');
    cy.get('#email').type('danielrmo95@gmail.com');
    cy.get('#password').type('Contrasena1');
    cy.get('#confirm-password').type('Contrasena1');
    cy.contains('button', 'Sign up').click();
    
    // Assert that the success message is displayed
    cy.contains('Successful registration!').should('be.visible');
  });
});
