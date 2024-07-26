describe('User Registration', () => {
  beforeEach(() => {
    cy.visit('https://test-qa.inlaze.com/auth/sign-in');
  });

  it('should show error message when passwords do not match ', () => {
    
    cy.get('#email').type('danielrmo95@gmail.com');
    cy.get('#password').type('Contrasena1');

      cy.contains('button', 'Sign in').click();
  });
});




