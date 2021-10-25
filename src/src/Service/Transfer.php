<?php
namespace App\Service;

use App\Entity\Transfer as EntityTransfer;
use App\Repository\CardRepository;
use App\Repository\PersonRepository;
use App\Repository\TransferRepository;

class Transfer 
{
    /** 
     * @var TransferRepository 
     * */
    private $repository;

    /**
     * @var PersonRepository
     */
    private $personRepository;

    /** 
     * @var CardRepository
     */
    private $cardRepository;

    public function __construct(
        TransferRepository $repository, 
        PersonRepository $personRepository,
        CardRepository $cardRepository
        )
    {
        $this->repository = $repository;
        $this->personRepository = $personRepository;
        $this->cardRepository = $cardRepository;
    }

    /**
     * 
     */
    public function list():array
    {
        return $this->repository->findAll();
    }

    public function listByUser($userId): ?array
    {
        return $this->repository->listByUser($userId);
    }

    /**
     * @var array $data
     * @return EntityTransfer
     */
    public function create(array $data): EntityTransfer
    {
        $friend = $this->personRepository->find($data['friend_id']);
        $card = $this->cardRepository->find($data['billing_card']['card_id']);
        $transfer = new EntityTransfer();
        $transfer
            ->setFriend($friend)
            ->setBillingCard($card)
            ->setTotalToTransfer($data['total_to_transfer'])
        ;
        return $this->repository->create($transfer);
    }

}