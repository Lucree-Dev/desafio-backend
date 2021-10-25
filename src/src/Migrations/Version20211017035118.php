<?php

declare(strict_types=1);

namespace DoctrineMigrations;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20211017035118 extends AbstractMigration
{
    public function getDescription() : string
    {
        return '';
    }

    public function up(Schema $schema) : void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->abortIf($this->connection->getDatabasePlatform()->getName() !== 'mysql', 'Migration can only be executed safely on \'mysql\'.');

        $this->addSql('CREATE TABLE card (id INT AUTO_INCREMENT NOT NULL, title VARCHAR(20) NOT NULL, pan VARCHAR(255) NOT NULL, expiry_mm VARCHAR(2) NOT NULL, expity_yyyy VARCHAR(4) NOT NULL, security_code VARCHAR(3) NOT NULL, date VARCHAR(10) NOT NULL, PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('CREATE TABLE person (id INT AUTO_INCREMENT NOT NULL, first_name VARCHAR(255) NOT NULL, last_name VARCHAR(255) NOT NULL, birthday DATE NOT NULL, password VARCHAR(255) NOT NULL, username VARCHAR(15) NOT NULL, PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('CREATE TABLE transfer (id INT AUTO_INCREMENT NOT NULL, friend_id INT NOT NULL, billing_card_id INT NOT NULL, total_to_transfer DOUBLE PRECISION NOT NULL, INDEX IDX_4034A3C06A5458E8 (friend_id), INDEX IDX_4034A3C021E211F7 (billing_card_id), PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('ALTER TABLE transfer ADD CONSTRAINT FK_4034A3C06A5458E8 FOREIGN KEY (friend_id) REFERENCES person (id)');
        $this->addSql('ALTER TABLE transfer ADD CONSTRAINT FK_4034A3C021E211F7 FOREIGN KEY (billing_card_id) REFERENCES card (id)');
        $this->addSql('CREATE TABLE fried (id INT AUTO_INCREMENT NOT NULL, person_id INT NOT NULL, friend_id INT NOT NULL, INDEX IDX_435D7EB217BBB47 (person_id), INDEX IDX_435D7EB6A5458E8 (friend_id), PRIMARY KEY(id)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
        $this->addSql('ALTER TABLE fried ADD CONSTRAINT FK_435D7EB217BBB47 FOREIGN KEY (person_id) REFERENCES person (id)');
        $this->addSql('ALTER TABLE fried ADD CONSTRAINT FK_435D7EB6A5458E8 FOREIGN KEY (friend_id) REFERENCES person (id)');
        
    }

    public function down(Schema $schema) : void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->abortIf($this->connection->getDatabasePlatform()->getName() !== 'mysql', 'Migration can only be executed safely on \'mysql\'.');

        $this->addSql('ALTER TABLE transfer DROP FOREIGN KEY FK_4034A3C021E211F7');
        $this->addSql('ALTER TABLE transfer DROP FOREIGN KEY FK_4034A3C06A5458E8');
        $this->addSql('DROP TABLE fried');
        $this->addSql('DROP TABLE card');
        $this->addSql('DROP TABLE person');
        $this->addSql('DROP TABLE transfer');
    }
}
