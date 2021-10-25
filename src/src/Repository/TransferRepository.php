<?php

namespace App\Repository;

use App\Entity\Transfer;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;

/**
 * @method Transfer|null find($id, $lockMode = null, $lockVersion = null)
 * @method Transfer|null findOneBy(array $criteria, array $orderBy = null)
 * @method Transfer[]    findAll()
 * @method Transfer[]    findBy(array $criteria, array $orderBy = null, $limit = null, $offset = null)
 */
class TransferRepository extends ServiceEntityRepository
{
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, Transfer::class);
    }

    /**
     * @param Transfer
     * @return Transfer
     */
    public function create(Transfer $transfer)
    {
        $this->getEntityManager()->persist($transfer);
        $this->getEntityManager()->flush();
        return $transfer;
    }

    public function listByUser($userId): ?array
    {
        $query = $this
            ->createQueryBuilder('t')
            ->innerJoin('t.billing_card', 'c')
            ->innerJoin('c.owner', 'o')
            ->andWhere('o.id = :userId')
            ->setParameter('userId', $userId)
            ->getQuery()
            ;
        return $query
            ->getResult()
        ;
    }
}
