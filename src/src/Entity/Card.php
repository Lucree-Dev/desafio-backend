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
    private $expity_yyyy;

    /**
     * @ORM\Column(type="string", length=3)
     */
    private $security_code;

    /**
     * @ORM\Column(type="string", length=10)
     */
    private $date;

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

    public function getExpityYyyy(): ?string
    {
        return $this->expity_yyyy;
    }

    public function setExpityYyyy(string $expity_yyyy): self
    {
        $this->expity_yyyy = $expity_yyyy;

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

    public function getDate(): ?string
    {
        return $this->date;
    }

    public function setDate(string $date): self
    {
        $this->date = $date;

        return $this;
    }
}
