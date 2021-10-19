<?php

namespace App\Entity;

use App\Repository\TransferRepository;
use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity(repositoryClass=TransferRepository::class)
 */
class Transfer
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer")
     */
    private $id;

    /**
     * @ORM\Column(type="float")
     */
    private $total_to_transfer;

    /**
     * @ORM\ManyToOne(targetEntity=Person::class)
     * @ORM\JoinColumn(nullable=false)
     */
    private $friend;

    /**
     * @ORM\ManyToOne(targetEntity=Card::class)
     * @ORM\JoinColumn(nullable=false)
     */
    private $billing_card;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getTotalToTransfer(): ?float
    {
        return $this->total_to_transfer;
    }

    public function setTotalToTransfer(float $total_to_transfer): self
    {
        $this->total_to_transfer = $total_to_transfer;

        return $this;
    }

    public function getFriend(): ?Person
    {
        return $this->friend;
    }

    public function setFriend(?Person $friend): self
    {
        $this->friend = $friend;

        return $this;
    }

    public function getBillingCard(): ?Card
    {
        return $this->billing_card;
    }

    public function setBillingCard(?Card $billing_card): self
    {
        $this->billing_card = $billing_card;

        return $this;
    }
}
