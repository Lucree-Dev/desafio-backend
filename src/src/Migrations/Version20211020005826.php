<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20211020005826 extends AbstractMigration
{
    public function getDescription() : string
    {
        return '';
    }

    public function up(Schema $schema) : void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->abortIf($this->connection->getDatabasePlatform()->getName() !== 'mysql', 'Migration can only be executed safely on \'mysql\'.');

        $this->addSql('ALTER TABLE card ADD owner_id INT NOT NULL, CHANGE date date DATE NOT NULL, CHANGE expity_yyyy expiry_yyyy VARCHAR(4) NOT NULL');
        $this->addSql('ALTER TABLE card ADD CONSTRAINT FK_161498D37E3C61F9 FOREIGN KEY (owner_id) REFERENCES person (id)');
        $this->addSql('CREATE INDEX IDX_161498D37E3C61F9 ON card (owner_id)');
    }

    public function down(Schema $schema) : void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->abortIf($this->connection->getDatabasePlatform()->getName() !== 'mysql', 'Migration can only be executed safely on \'mysql\'.');

        $this->addSql('ALTER TABLE card DROP FOREIGN KEY FK_161498D37E3C61F9');
        $this->addSql('DROP INDEX IDX_161498D37E3C61F9 ON card');
        $this->addSql('ALTER TABLE card DROP owner_id, CHANGE date date VARCHAR(10) CHARACTER SET utf8mb4 NOT NULL COLLATE `utf8mb4_unicode_ci`, CHANGE expiry_yyyy expity_yyyy VARCHAR(4) CHARACTER SET utf8mb4 NOT NULL COLLATE `utf8mb4_unicode_ci`');
    }
}
