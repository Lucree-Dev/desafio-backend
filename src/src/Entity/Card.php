<?php

namespace App\Entity;

use App\Repository\CardRepository;
use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity(repositoryClass=CardRepository::class)
 */
class Card
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer")
     */
    private $id;

    /**
     * @ORM\Column(type="string", length=20)
     */
    private $title;

    /**
     * @ORM\Column(type="string", length=255)
     */
    private $pan;

    /**
     * @ORM\Column(type="string", length=2)
     */
    private $expiry_mm;

    /**
     * @ORM\Column(type="string", length=4)
     */
    private $expiry_yyyy;

    /**
     * @ORM\Column(type="string", length=3)
     */
    private $security_code;

    /**
     * @ORM\Column(type="date", length=10)
     */
    private $date;

    /**
     * @ORM\ManyToOne(targetEntity=Person::class)
     * @ORM\JoinColumn(nullable=false)
     */
    private $owner;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getTitle(): ?string
    {
        return $this->title;
    }

    public function setTitle(string $title): self
    {
        $this->title = $title;

        return $this;
    }

    public function getPan(): ?string
    {
        return $this->pan;
    }

    public function setPan(string $pan): self
    {
        $this->pan = $pan;

        return $this;
    }

    public function getExpiryMm(): ?string
    {
        return $this->expiry_mm;
    }

    public function setExpiryMm(string $expiry_mm): self
    {
        $this->expiry_mm = $expiry_mm;

        return $this;
    }

    public function getExpryYyyy(): ?string
    {
        return $this->expiry_yyyy;
    }

    public function setExpiryYyyy(string $expity_yyyy): self
    {
        $this->expiry_yyyy = $expity_yyyy;
        return $this;
    }

    public function getSecurityCode(): ?string
    {
        return $this->security_code;
    }

    public function setSecurityCode(string $security_code): self
    {
        $this->security_code = $security_code;

        return $this;
    }

    public function getDate(): \DateTime
    {
        return $this->date;
    }

    public function setDate(\DateTime $date): self
    {
        $this->date = $date;

        return $this;
    }

    /**
     * Get the value of owner
     */ 
    public function getOwner(): Person
    {
        return $this->owner;
    }

    /**
     * Set the value of owner
     * @return  self
     */ 
    public function setOwner(Person $owner): self
    {
        $this->owner = $owner;
        return $this;
    }
}
