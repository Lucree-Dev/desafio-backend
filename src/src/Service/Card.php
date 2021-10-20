<?php
namespace App\Service;

use App\Entity\Card as EntityCard;
use App\Repository\CardRepository;
use App\Repository\PersonRepository;

class Card 
{
    /** 
     * @var CardRepository 
     * */
    private $repository;

    /**
     * @var PersonRepository
     */
    private $personRepository;

    public function __construct(CardRepository $repository, PersonRepository $personRepository)
    {
        $this->repository = $repository;
        $this->personRepository = $personRepository;
    }

    /**
     * 
     */
    public function list():array
    {
        return $this->repository->findAll();
    }

    /**
     * @var array $data
     * @return EntityCard
     */
    public function create(array $data): EntityCard
    {
        $owner = $data['owner'];
        if (!$owner instanceof Person) {
            $owner = $this->personRepository->find($owner);
        }
        $date = $data['date'];
        if (!$date instanceof \DateTime) {
            $date = \DateTime::createFromFormat('Y-m-d', $data['date']);
        }
        /** @var EntityCard */
        $card = new EntityCard();
        $card
            ->setTitle($data['title'])
            ->setPan($data['pan'])
            ->setExpiryMm($data['expiry_mm'])
            ->setExpiryYyyy($data['expiry_yyyy'])
            ->setSecurityCode($data['security_code'])
            ->setDate($date)
            ->setOwner($owner)
        ;
        return $this->repository->create($card);
    }

    public function get($id)
    {

    }
}
